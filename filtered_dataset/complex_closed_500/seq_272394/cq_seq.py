import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03875, 0.00237).lineTo(-0.02975, 0.00237).threePointArc((-0.02869, 0.00194), (-0.02825, 0.00087)).lineTo(-0.02825, -0.00088).threePointArc((-0.02869, -0.00194), (-0.02975, -0.00238)).lineTo(-0.03875, -0.00238).threePointArc((-0.03981, -0.00194), (-0.04025, -0.00088)).lineTo(-0.04025, 0.00087).threePointArc((-0.03981, 0.00194), (-0.03875, 0.00237)).close()
solid=wp_sketch0.add(loop0).extrude(-0.0009782290225170273)
