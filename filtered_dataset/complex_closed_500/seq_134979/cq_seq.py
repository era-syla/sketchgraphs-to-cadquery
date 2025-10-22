import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.019, 0.0076).lineTo(0.009, 0.0076).lineTo(0.009, 0.0).lineTo(0.019, 0.0).lineTo(0.019, 0.0076).close()
solid=wp_sketch0.add(loop0).extrude(0.020012843038551935)
