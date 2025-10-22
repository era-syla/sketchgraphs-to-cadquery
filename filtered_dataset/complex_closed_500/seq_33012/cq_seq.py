import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0193, 0.01959).lineTo(0.0113, 0.01959).lineTo(0.0113, 0.01179).lineTo(0.0193, 0.01179).lineTo(0.0193, 0.01959).close()
solid=wp_sketch0.add(loop0).extrude(-0.013737394061088874)
