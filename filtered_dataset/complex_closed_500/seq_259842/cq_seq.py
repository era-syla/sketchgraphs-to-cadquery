import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.14814, 0.0486).lineTo(-0.14814, 0.04787).lineTo(-0.14858, 0.04829).lineTo(-0.14814, 0.0486).close()
solid=wp_sketch0.add(loop0).extrude(-0.0019356032570153636)
