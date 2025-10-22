import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.8636, 0.0).lineTo(0.8636, 0.9144).lineTo(-0.0, 0.9144).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.7692600016640891)
