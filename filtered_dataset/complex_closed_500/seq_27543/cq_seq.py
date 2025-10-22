import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0215, 0.0965).lineTo(-0.0215, 0.0965).lineTo(-0.0215, 0.155).lineTo(0.0215, 0.155).lineTo(0.0215, 0.0965).close()
solid=wp_sketch0.add(loop0).extrude(-0.09210221905112424)
