import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0514, -0.04693).lineTo(-0.0514, -0.04693).threePointArc((-0.05589, -0.04507), (-0.05775, -0.04058)).lineTo(-0.05775, 0.04058).threePointArc((-0.05589, 0.04507), (-0.0514, 0.04693)).lineTo(0.0514, 0.04693).threePointArc((0.05589, 0.04507), (0.05775, 0.04058)).lineTo(0.05775, -0.04058).threePointArc((0.05589, -0.04507), (0.0514, -0.04693)).close()
solid=wp_sketch0.add(loop0).extrude(-0.33459393150557215)
