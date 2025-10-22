import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00933, -0.01296).threePointArc((-0.0, -0.00933), (-0.00933, -0.01296)).lineTo(-0.01393, -0.00441).lineTo(-0.00678, -0.00045).lineTo(0.00633, -0.00045).lineTo(0.01596, -0.00576).lineTo(0.00933, -0.01296).close()
solid=wp_sketch0.add(loop0).extrude(-0.0668780337358687)
