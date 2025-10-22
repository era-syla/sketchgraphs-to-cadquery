import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00781, 0.0).threePointArc((0.01364, 0.00067), (0.01925, 0.0024)).lineTo(0.01925, -0.0).lineTo(0.00781, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.016306799254847175)
