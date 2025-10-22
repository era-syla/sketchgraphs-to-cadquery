import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0123, 0.002).lineTo(0.0143, 0.002).lineTo(0.0143, -0.002).lineTo(0.0123, -0.002).lineTo(0.0123, 0.002).close()
solid=wp_sketch0.add(loop0).extrude(0.00010479448552454685)
