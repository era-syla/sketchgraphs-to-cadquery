import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.05236, 0.03752).threePointArc((0.03221, 0.05578), (0.00631, 0.0641)).threePointArc((0.00181, 0.06637), (-0.0, 0.07107)).lineTo(0.0, 0.09594).threePointArc((0.00223, 0.10107), (0.00751, 0.10292)).threePointArc((0.0516, 0.08937), (0.08538, 0.05796)).threePointArc((0.08641, 0.05247), (0.08309, 0.04797)).lineTo(0.06155, 0.03553).threePointArc((0.05657, 0.03475), (0.05236, 0.03752)).close()
solid=wp_sketch0.add(loop0).extrude(-0.20172232256290082)
