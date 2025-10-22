import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(3.048, 1.8288).lineTo(-3.048, 1.8288).lineTo(-3.048, -1.8288).lineTo(3.048, -1.8288).lineTo(3.048, 1.8288).close()
solid=wp_sketch0.add(loop0).extrude(17.57470102756039)
