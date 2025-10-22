import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.05909, 0.00085).lineTo(0.04653, 0.0081).threePointArc((0.04633, 0.00844), (0.04653, 0.00879)).lineTo(0.05909, 0.01604).threePointArc((0.05949, 0.01604), (0.05969, 0.01569)).lineTo(0.05969, 0.00119).threePointArc((0.05949, 0.00085), (0.05909, 0.00085)).close()
solid=wp_sketch0.add(loop0).extrude(-0.03167163737569455)
