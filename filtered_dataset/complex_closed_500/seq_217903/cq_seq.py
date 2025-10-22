import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.07522, 0.05485).lineTo(-0.07278, 0.05485).lineTo(-0.07278, 0.00135).lineTo(0.07522, 0.00135).lineTo(0.07522, 0.05485).close()
solid=wp_sketch0.add(loop0).extrude(0.06601499750706878)
