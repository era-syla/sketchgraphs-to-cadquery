import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0094, -0.0094).lineTo(-0.0094, -0.0094).lineTo(-0.0094, 0.0094).lineTo(0.0094, 0.0094).lineTo(0.0094, -0.0094).close()
solid=wp_sketch0.add(loop0).extrude(0.03994591250726441)
