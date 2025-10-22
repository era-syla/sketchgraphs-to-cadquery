import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.17593, 0.72632).lineTo(-0.1679, 0.72632).threePointArc((-0.19484, 0.71516), (-0.206, 0.68822)).lineTo(-0.206, -0.77141).lineTo(-0.20133, -0.7938).lineTo(0.20798, -0.7938).lineTo(0.21403, -0.7858).lineTo(0.21403, 0.68822).threePointArc((0.20287, 0.71516), (0.17593, 0.72632)).close()
solid=wp_sketch0.add(loop0).extrude(-0.9316198461076687)
