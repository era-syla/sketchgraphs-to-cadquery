import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02493, -0.02699).threePointArc((0.00122, 0.03672), (-0.02667, -0.02527)).lineTo(-0.02667, -0.03863).threePointArc((0.00104, 0.04693), (0.02493, -0.03978)).lineTo(0.02493, -0.02699).close()
solid=wp_sketch0.add(loop0).extrude(-0.26798059782317935)
