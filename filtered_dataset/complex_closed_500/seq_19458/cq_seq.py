import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.11704, 0.0368).lineTo(-0.07935, 0.0368).lineTo(-0.07935, 0.05233).lineTo(-0.11704, 0.05233).lineTo(-0.11704, 0.0368).close()
solid=wp_sketch0.add(loop0).extrude(-0.07683742330431695)
