import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05696, 0.0).lineTo(0.07504, 0.0).lineTo(0.07504, -0.07538).lineTo(-0.05696, -0.07538).lineTo(-0.05696, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.3817041469354792)
