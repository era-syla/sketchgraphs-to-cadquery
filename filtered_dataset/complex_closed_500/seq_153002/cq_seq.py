import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03175, 0.0).lineTo(0.03175, 0.0).lineTo(0.03175, 0.00064).lineTo(-0.03175, 0.00064).lineTo(-0.03175, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.08321656250818682)
