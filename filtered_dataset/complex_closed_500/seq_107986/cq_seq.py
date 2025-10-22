import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01, -0.02788).lineTo(-0.01, -0.02788).lineTo(-0.01, 0.02788).lineTo(0.01, 0.02788).lineTo(0.01, -0.02788).close()
solid=wp_sketch0.add(loop0).extrude(0.11636437016728386)
