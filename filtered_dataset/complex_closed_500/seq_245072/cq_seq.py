import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.46843, 1.21047).lineTo(-0.7125, -0.00706).lineTo(-0.85522, 0.02155).lineTo(-0.61115, 1.23908).lineTo(-0.46843, 1.21047).close()
solid=wp_sketch0.add(loop0).extrude(0.055873960233042794)
