import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03048, 0.02286).threePointArc((-0.05015, 0.01672), (-0.0381, 0.0)).lineTo(0.0, 0.0).lineTo(0.0, 0.0127).threePointArc((-0.01606, 0.01531), (-0.03048, 0.02286)).close()
solid=wp_sketch0.add(loop0).extrude(-0.02652666250627753)
