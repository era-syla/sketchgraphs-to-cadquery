import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01098, 0.07017).lineTo(-0.05302, 0.07017).lineTo(-0.05302, 0.07517).lineTo(0.01098, 0.07517).lineTo(0.01098, 0.07017).close()
solid=wp_sketch0.add(loop0).extrude(0.009043643655539824)
