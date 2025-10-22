import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.002, 0.0032).lineTo(0.035, 0.0032).lineTo(0.035, -0.0033).lineTo(0.002, -0.0033).lineTo(0.002, 0.0032).close()
solid=wp_sketch0.add(loop0).extrude(-0.011945108901424278)
