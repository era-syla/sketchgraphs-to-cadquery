import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01227, 0.0604).lineTo(-0.03042, 0.0604).lineTo(-0.04409, 0.0604).lineTo(-0.04409, 0.0534).lineTo(0.00141, 0.0534).lineTo(0.00141, 0.0604).lineTo(-0.01227, 0.0604).close()
solid=wp_sketch0.add(loop0).extrude(0.04005243048053468)
