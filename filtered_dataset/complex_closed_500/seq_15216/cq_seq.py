import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00225, 0.07682).lineTo(0.00225, 0.07682).lineTo(0.00225, 0.01646).lineTo(-0.00225, 0.01646).lineTo(-0.00225, 0.07682).close()
solid=wp_sketch0.add(loop0).extrude(0.07119389762015209)
