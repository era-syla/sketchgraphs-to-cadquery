import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00193, -0.01094).lineTo(-0.00193, -0.00706).lineTo(-0.0055, -0.005).lineTo(-0.0, -0.005).lineTo(0.0, -0.013).lineTo(-0.0055, -0.013).lineTo(-0.00193, -0.01094).close()
solid=wp_sketch0.add(loop0).extrude(0.013459083032653986)
