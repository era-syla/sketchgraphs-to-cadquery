import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.12837, 0.03493).lineTo(0.13315, 0.03493).threePointArc((0.13764, 0.03307), (0.1395, 0.02858)).lineTo(0.1395, -0.0381).threePointArc((0.13764, -0.04259), (0.13315, -0.04445)).lineTo(0.12837, -0.04445).threePointArc((0.12388, -0.04259), (0.12202, -0.0381)).lineTo(0.12202, 0.02858).threePointArc((0.12388, 0.03307), (0.12837, 0.03493)).close()
solid=wp_sketch0.add(loop0).extrude(0.010956839053437799)
