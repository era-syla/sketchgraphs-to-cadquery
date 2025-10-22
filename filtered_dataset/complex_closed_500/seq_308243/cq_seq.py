import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.03862, 0.0).lineTo(0.04762, 0.009).lineTo(0.04762, 0.021).lineTo(0.03862, 0.03).lineTo(0.0, 0.03).threePointArc((-0.015, 0.015), (-0.0, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(-0.06265935349992105)
