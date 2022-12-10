#version 150

uniform sampler2D DiffuseSampler;
uniform sampler2D PrevSampler;
uniform sampler2D VariableSampler;
uniform sampler2D JudgeSampler;

uniform float Time;
in vec2 texCoord;
in vec2 oneTexel;

uniform vec2 InSize;

out vec4 fragColor;

#define PI 3.1415926535897932384626433832795

#define VAR_FPS_TEST 0.0
#define VAR_FPS 1.0
#define VAR_SHAKE_FRAME 2.0

int imod(int num, int m) {
	return num - (num / m * m);
}

int getVar(sampler2D sampler, float id) {
	vec4 var_color = texture(sampler, vec2((id + 0.5) * 0.01, 0.0));
	return int(var_color.r * 255.0)/4*4096 + int(var_color.g * 255.0)/4*64 + int(var_color.b * 255.0)/4;
}

vec3 hue(float h) {
    float r = abs(h * 6.0 - 3.0) - 1.0;
    float g = 2.0 - abs(h * 6.0 - 2.0);
    float b = 2.0 - abs(h * 6.0 - 4.0);
    return clamp(vec3(r,g,b), 0.0, 1.0);
}

vec3 HSVtoRGB(vec3 hsv) {
    return ((hue(hsv.x) - 1.0) * hsv.y + 1.0) * hsv.z;
}

vec3 RGBtoHSV(vec3 rgb) {
    vec3 hsv = vec3(0.0);
    hsv.z = max(rgb.r, max(rgb.g, rgb.b));
    float min = min(rgb.r, min(rgb.g, rgb.b));
    float c = hsv.z - min;

    if (c != 0.0)
    {
        hsv.y = c / hsv.z;
        vec3 delta = (hsv.z - rgb) / c;
        delta.rgb -= delta.brg;
        delta.rg += vec2(2.0, 4.0);
        if (rgb.r >= hsv.z) {
            hsv.x = delta.b;
        } else if (rgb.g >= hsv.z) {
            hsv.x = delta.r;
        } else {
            hsv.x = delta.g;
        }
        hsv.x = fract(hsv.x / 6.0);
    }
    return hsv;
}

vec4 blendOver(vec4 over, vec4 base) {
	vec3 colorA = over.rgb * over.a + base.rgb * base.a * (1 - over.a);
	float alpha = over.a + base.a * (1 - over.a);
	return vec4(colorA / alpha, alpha);
}



void main() {
	vec4 PrevTexel = texture(PrevSampler, texCoord);
	vec4 CurrTexel = texture(DiffuseSampler, texCoord);
	vec4 JudgeTexel = texture(JudgeSampler, texCoord);
	fragColor = vec4(0.0, 0.0, 0.0, 0.0);
	
	if (CurrTexel.r > 0.996 && CurrTexel.g < 0.004 && CurrTexel.b < 0.004)
		fragColor = PrevTexel;
	else if (JudgeTexel.a > 0.9) {
		float flash = 0.0;
		if (mod(Time, 0.1) > 0.05)
			flash = 0.5;
		fragColor = vec4(0.0, 0.0, 0.0, flash);
	}
}
