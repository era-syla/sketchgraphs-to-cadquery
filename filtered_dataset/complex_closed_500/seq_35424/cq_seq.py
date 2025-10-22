import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.009, 0.014).lineTo(0.012, 0.014).lineTo(0.012, 0.003).lineTo(0.009, 0.014).close()
solid=wp_sketch0.add(loop0).extrude(0.02601788912276318)
