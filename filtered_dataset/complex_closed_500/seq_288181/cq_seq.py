import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.03645, 0.6096).lineTo(0.03645, -0.6096).lineTo(0.79845, -0.6096).lineTo(0.79845, 0.0).lineTo(0.29045, -0.0).lineTo(0.16345, 0.6096).lineTo(0.03645, 0.6096).close()
solid=wp_sketch0.add(loop0).extrude(1.6286684112967018)
