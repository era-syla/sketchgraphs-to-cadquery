import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.005, 0.0).lineTo(-0.008, 0.0).lineTo(-0.008, 0.003).threePointArc((-0.00588, 0.00212), (-0.005, -0.0)).close()
solid=wp_sketch0.add(loop0).extrude(-0.004824376875886955)
