import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03415, 0.01315).lineTo(0.03385, 0.01315).lineTo(0.03385, 0.00715).lineTo(-0.03415, 0.00715).lineTo(-0.03415, 0.01315).close()
solid=wp_sketch0.add(loop0).extrude(-0.0774571326043818)
