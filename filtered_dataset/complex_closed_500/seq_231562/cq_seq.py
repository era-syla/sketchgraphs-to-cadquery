import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02355, 0.04111).lineTo(0.02355, 0.02511).lineTo(0.01555, 0.02511).threePointArc((-0.00445, 0.01549), (-0.02445, 0.02511)).lineTo(-0.03245, 0.02511).lineTo(-0.03245, 0.04111).lineTo(-0.02445, 0.04111).threePointArc((-0.00445, 0.02111), (0.01555, 0.04111)).lineTo(0.02355, 0.04111).close()
solid=wp_sketch0.add(loop0).extrude(-0.023016915371372938)
