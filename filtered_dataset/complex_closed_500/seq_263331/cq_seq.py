import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0635, 0.0381).lineTo(0.0635, 0.0381).lineTo(0.0635, -0.0635).lineTo(-0.0635, -0.0635).lineTo(-0.0635, 0.0381).close()
solid=wp_sketch0.add(loop0).extrude(0.21496752511424647)
