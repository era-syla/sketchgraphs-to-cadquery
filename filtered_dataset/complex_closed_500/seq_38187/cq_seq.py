import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0185, 0.0).lineTo(0.0185, 0.0).lineTo(0.0185, 0.00763).lineTo(-0.0185, 0.00763).lineTo(-0.0185, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.05990469159931573)
