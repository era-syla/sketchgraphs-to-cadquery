import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.15588, 0.0).lineTo(-0.68928, 0.0).lineTo(-0.68928, 0.0381).lineTo(-0.72738, 0.0381).lineTo(-0.72738, 0.5715).lineTo(-0.68928, 0.5715).lineTo(-0.68928, 0.6096).lineTo(-0.15588, 0.6096).lineTo(-0.15588, 0.5715).lineTo(-0.11778, 0.5715).lineTo(-0.11778, 0.0381).lineTo(-0.15588, 0.0381).lineTo(-0.15588, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(1.6771295605235266)
