import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0175, 0.015).lineTo(0.0175, 0.015).lineTo(0.0175, 0.006).lineTo(-0.0175, 0.006).lineTo(-0.0175, 0.015).close()
solid=wp_sketch0.add(loop0).extrude(0.008401461320686998)
