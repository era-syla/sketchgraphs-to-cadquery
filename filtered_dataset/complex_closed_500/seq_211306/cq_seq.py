import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.14363, -0.09188).lineTo(-0.14363, -0.09188).lineTo(-0.14363, 0.09188).lineTo(0.14363, 0.09188).lineTo(0.14363, -0.09188).close()
solid=wp_sketch0.add(loop0).extrude(0.6643139070710066)
