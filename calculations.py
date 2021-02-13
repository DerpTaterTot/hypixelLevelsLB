class calculations():
    def __init__(self) -> None:
        pass
    
    def skywarsLevel(self, xp):
        xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
        if xp >= 15000:
            return (xp - 15000) / 10000. + 12
        else:
            for i in range(len(xps)):
                if xp < xps[i]:
                    return 1 + i + float(xp - xps[i-1]) / (xps[i] - xps[i-1])
                