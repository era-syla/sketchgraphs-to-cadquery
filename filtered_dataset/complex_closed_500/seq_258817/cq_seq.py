import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00261, -0.02033).threePointArc((0.00044, -0.0205), (0.00348, -0.0202)).lineTo(0.00399, -0.02316).threePointArc((0.0005, -0.02349), (-0.00299, -0.02331)).lineTo(-0.00261, -0.02033).close()
solid=wp_sketch0.add(loop0).extrude(0.01206321806194929)
