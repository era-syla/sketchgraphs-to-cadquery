import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0148, 0.00935).lineTo(-0.0148, 0.00697).lineTo(-0.01466, 0.00697).lineTo(-0.01466, 0.00935).lineTo(-0.0148, 0.00935).close()
solid=wp_sketch0.add(loop0).extrude(0.0015907414096070626)
