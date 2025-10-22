import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.03, 0.0).lineTo(0.03, 0.03).lineTo(0.035, 0.03).lineTo(0.035, -0.0197).lineTo(0.1045, -0.0197).lineTo(0.1045, -0.0247).lineTo(0.0, -0.0247).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.2924611841107779)
