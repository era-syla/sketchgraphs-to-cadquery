import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.17513, 0.18632).lineTo(0.41363, 0.18632).lineTo(0.41363, -0.01368).lineTo(0.17513, -0.01368).lineTo(0.17513, 0.18632).close()
solid=wp_sketch0.add(loop0).extrude(-0.6473956381401431)
