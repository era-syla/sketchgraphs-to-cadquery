import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.018, 0.019).threePointArc((-0.02151, 0.02749), (-0.03, 0.031)).lineTo(0.03, 0.031).threePointArc((0.02151, 0.02749), (0.018, 0.019)).lineTo(0.018, 0.017).threePointArc((0.01507, 0.00993), (0.008, 0.007)).lineTo(-0.008, 0.007).threePointArc((-0.01507, 0.00993), (-0.018, 0.017)).lineTo(-0.018, 0.019).close()
solid=wp_sketch0.add(loop0).extrude(0.024133877190668007)
