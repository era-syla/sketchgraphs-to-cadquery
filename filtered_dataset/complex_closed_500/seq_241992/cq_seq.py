import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.035, 0.0).lineTo(-0.035, 0.024).lineTo(-0.0, 0.024).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.06963362591490838)
