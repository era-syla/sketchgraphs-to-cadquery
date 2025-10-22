import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.042, 0.03).lineTo(0.042, 0.03).threePointArc((0.04907, 0.02707), (0.052, 0.02)).lineTo(0.052, -0.02).threePointArc((0.04907, -0.02707), (0.042, -0.03)).lineTo(-0.042, -0.03).threePointArc((-0.04907, -0.02707), (-0.052, -0.02)).lineTo(-0.052, 0.02).threePointArc((-0.04907, 0.02707), (-0.042, 0.03)).close()
solid=wp_sketch0.add(loop0).extrude(-0.2956366833371247)
