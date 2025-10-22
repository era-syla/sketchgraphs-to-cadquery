import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(6.9723, 0.2032).lineTo(6.2103, 0.2032).lineTo(6.2103, 2.3368).lineTo(6.9723, 2.3368).lineTo(6.9723, 0.2032).close()
solid=wp_sketch0.add(loop0).extrude(3.8717603358071444)
