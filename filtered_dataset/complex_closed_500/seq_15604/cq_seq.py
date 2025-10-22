import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.16, -0.19).lineTo(-0.16, -0.19).threePointArc((-0.18121, -0.18121), (-0.19, -0.16)).lineTo(-0.19, 0.16).threePointArc((-0.18121, 0.18121), (-0.16, 0.19)).lineTo(0.16, 0.19).threePointArc((0.18121, 0.18121), (0.19, 0.16)).lineTo(0.19, -0.16).threePointArc((0.18121, -0.18121), (0.16, -0.19)).close()
solid=wp_sketch0.add(loop0).extrude(-1.0196952399122057)
