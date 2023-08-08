//!DESC noise (luma, adaptive)
//!HOOK LUMA
//!HOOK RGB
//!BIND HOOKED
//!WIDTH OUTPUT.w
//!HEIGHT OUTPUT.h

#define STRENGTH 64.0
#define LUMA_SCALING 10.0

// PRNG taken from mpv's shader
float mod289(float x)  { return x - floor(x / 289.0) * 289.0; }
float permute(float x) { return mod289((34.0 * x + 1.0) * x); }
float rand(float x)    { return fract(x / 41.0); }

vec4 hook() {
    vec2 uv = HOOKED_pos.xy;
    vec4 originalColor = HOOKED_tex(uv);

    float x = dot(originalColor.rgb, vec3(0.2989, 0.5870, 0.1140)); // Convert to luma
    float y = LUMA_SCALING * 0.5; // Average luma can't be computed from a shader, fake it...

    // https://blog.kageru.moe/legacy/adaptivegrain.html
    float polynomial = 1.0 - (
        1.124 * x - 9.466 * x * x + 36.624 * x * x * x - 
        45.47 * x * x * x * x + 18.188 * x * x * x * x * x
    );

    float exponent = y * y;
    float z = pow(polynomial, exponent);

    // Generate noise based on the pixel's position
    vec3 _m = vec3(HOOKED_pos, random) + vec3(1.0);
    float h = permute(permute(permute(_m.x) + _m.y) + _m.z);
    float noise = STRENGTH / 4096.0 * (rand(h) - 0.5);

    // Apply the polynomial to the noise
    float scaledNoise = noise * z;

    vec4 resultColor = originalColor + vec4(scaledNoise);

    return resultColor;
}
