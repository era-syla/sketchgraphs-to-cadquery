import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02351, 0.02851).threePointArc((-0.03695, 0.0), (0.02351, -0.02851)).lineTo(0.06132, -0.02851).lineTo(0.06132, 0.02851).lineTo(0.02351, 0.02851).close()
solid=wp_sketch0.add(loop0).extrude(0.027988061894439815)
